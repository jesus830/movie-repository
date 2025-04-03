#include "MovieRepository.h"
#include <aws/dynamodb/model/CreateTableRequest.h>
#include <aws/dynamodb/model/DeleteTableRequest.h>
#include <aws/dynamodb/model/DescribeTableRequest.h>
#include <aws/dynamodb/model/ListTablesRequest.h>
#include <aws/dynamodb/model/PutItemRequest.h>
#include <aws/dynamodb/model/GetItemRequest.h>
#include <aws/dynamodb/model/UpdateItemRequest.h>
#include <aws/dynamodb/model/DeleteItemRequest.h>
#include <aws/dynamodb/model/QueryRequest.h>
#include <aws/dynamodb/model/ScanRequest.h>
#include <aws/dynamodb/model/BatchWriteItemRequest.h>
#include <aws/dynamodb/model/WriteRequest.h>
#include <aws/core/utils/Outcome.h>
#include <iostream>
#include <thread>
#include <chrono>

namespace AmazonQCustomizationDemo {

MovieRepository::MovieRepository(const Aws::Client::ClientConfiguration* clientConfig, 
                               const std::string& tableName)
    : m_tableName(tableName) {
    
    if (clientConfig) {
        m_dynamoDbClient = std::make_shared<Aws::DynamoDB::DynamoDBClient>(*clientConfig);
    } else {
        m_dynamoDbClient = std::make_shared<Aws::DynamoDB::DynamoDBClient>();
    }

    // Check if the table exists
    if (tableName != "") {
        Exists(tableName);
    }
}

MovieRepository::~MovieRepository() {
    // Cleanup is handled by smart pointers
}

bool MovieRepository::Exists(const std::string& tableName) {
    Aws::DynamoDB::Model::DescribeTableRequest request;
    request.SetTableName(tableName);

    try {
        auto outcome = m_dynamoDbClient->DescribeTable(request);
        if (outcome.IsSuccess()) {
            m_tableName = tableName;
            return true;
        }
    } catch (const Aws::DynamoDB::DynamoDBException& e) {
        if (e.GetErrorType() != Aws::DynamoDB::DynamoDBErrors::RESOURCE_NOT_FOUND) {
            std::cerr << "Error checking if table exists: " << e.what() << std::endl;
        }
    }
    return false;
}

bool MovieRepository::CreateTable(const std::string& tableName) {
    Aws::DynamoDB::Model::CreateTableRequest request;
    
    Aws::DynamoDB::Model::AttributeDefinition yearAttribute;
    yearAttribute.SetAttributeName("year");
    yearAttribute.SetAttributeType(Aws::DynamoDB::Model::ScalarAttributeType::N);
    
    Aws::DynamoDB::Model::AttributeDefinition titleAttribute;
    titleAttribute.SetAttributeName("title");
    titleAttribute.SetAttributeType(Aws::DynamoDB::Model::ScalarAttributeType::S);
    
    request.AddAttributeDefinitions(yearAttribute);
    request.AddAttributeDefinitions(titleAttribute);
    
    Aws::DynamoDB::Model::KeySchemaElement yearKeySchema;
    yearKeySchema.WithAttributeName("year").WithKeyType(Aws::DynamoDB::Model::KeyType::HASH);
    
    Aws::DynamoDB::Model::KeySchemaElement titleKeySchema;
    titleKeySchema.WithAttributeName("title").WithKeyType(Aws::DynamoDB::Model::KeyType::RANGE);
    
    request.AddKeySchema(yearKeySchema);
    request.AddKeySchema(titleKeySchema);
    
    Aws::DynamoDB::Model::ProvisionedThroughput throughput;
    throughput.WithReadCapacityUnits(10).WithWriteCapacityUnits(10);
    request.SetProvisionedThroughput(throughput);
    
    request.SetTableName(tableName);
    
    try {
        auto outcome = m_dynamoDbClient->CreateTable(request);
        if (outcome.IsSuccess()) {
            m_tableName = tableName;
            
            // Wait for the table to become active
            bool tableActive = false;
            while (!tableActive) {
                Aws::DynamoDB::Model::DescribeTableRequest describeRequest;
                describeRequest.SetTableName(tableName);
                
                auto describeOutcome = m_dynamoDbClient->DescribeTable(describeRequest);
                if (describeOutcome.IsSuccess()) {
                    auto status = describeOutcome.GetResult().GetTable().GetTableStatus();
                    tableActive = status == Aws::DynamoDB::Model::TableStatus::ACTIVE;
                }
                
                if (!tableActive) {
                    std::this_thread::sleep_for(std::chrono::seconds(1));
                }
            }
            
            return true;
        } else {
            std::cerr << "Failed to create table: " << outcome.GetError().GetMessage() << std::endl;
        }
    } catch (const Aws::DynamoDB::DynamoDBException& e) {
        std::cerr << "Error creating table: " << e.what() << std::endl;
    }
    
    return false;
}

std::vector<std::string> MovieRepository::ListTables() {
    std::vector<std::string> tableNames;
    Aws::DynamoDB::Model::ListTablesRequest request;
    
    try {
        bool moreTablesRemaining = true;
        while (moreTablesRemaining) {
            auto outcome = m_dynamoDbClient->ListTables(request);
            if (outcome.IsSuccess()) {
                for (const auto& tableName : outcome.GetResult().GetTableNames()) {
                    tableNames.push_back(tableName);
                    std::cout << tableName << std::endl;
                }
                
                if (outcome.GetResult().GetLastEvaluatedTableName().empty()) {
                    moreTablesRemaining = false;
                } else {
                    request.SetExclusiveStartTableName(outcome.GetResult().GetLastEvaluatedTableName());
                }
            } else {
                std::cerr << "Failed to list tables: " << outcome.GetError().GetMessage() << std::endl;
                moreTablesRemaining = false;
            }
        }
    } catch (const Aws::DynamoDB::DynamoDBException& e) {
        std::cerr << "Error listing tables: " << e.what() << std::endl;
    }
    
    return tableNames;
}

bool MovieRepository::Insert(const std::string& title, int year, const std::string& plot, double rating) {
    Aws::DynamoDB::Model::PutItemRequest request;
    request.SetTableName(m_tableName);
    
    Aws::DynamoDB::Model::AttributeValue yearAttr;
    yearAttr.SetN(std::to_string(year));
    
    Aws::DynamoDB::Model::AttributeValue titleAttr;
    titleAttr.SetS(title);
    
    Aws::DynamoDB::Model::AttributeValue infoAttr;
    Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue> infoMap;
    
    Aws::DynamoDB::Model::AttributeValue plotAttr;
    plotAttr.SetS(plot);
    infoMap["plot"] = plotAttr;
    
    Aws::DynamoDB::Model::AttributeValue ratingAttr;
    ratingAttr.SetN(std::to_string(rating));
    infoMap["rating"] = ratingAttr;
    
    infoAttr.SetM(infoMap);
    
    Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue> item;
    item["year"] = yearAttr;
    item["title"] = titleAttr;
    item["info"] = infoAttr;
    
    request.SetItem(item);
    
    try {
        auto outcome = m_dynamoDbClient->PutItem(request);
        if (outcome.IsSuccess()) {
            return true;
        } else {
            std::cerr << "Failed to add movie: " << outcome.GetError().GetMessage() << std::endl;
        }
    } catch (const Aws::DynamoDB::DynamoDBException& e) {
        std::cerr << "Error adding movie: " << e.what() << std::endl;
    }
    
    return false;
}

std::map<std::string, Aws::DynamoDB::Model::AttributeValue> MovieRepository::Select(const std::string& title, int year) {
    Aws::DynamoDB::Model::GetItemRequest request;
    request.SetTableName(m_tableName);
    
    Aws::DynamoDB::Model::AttributeValue yearAttr;
    yearAttr.SetN(std::to_string(year));
    
    Aws::DynamoDB::Model::AttributeValue titleAttr;
    titleAttr.SetS(title);
    
    request.AddKey("year", yearAttr);
    request.AddKey("title", titleAttr);
    
    try {
        auto outcome = m_dynamoDbClient->GetItem(request);
        if (outcome.IsSuccess()) {
            return outcome.GetResult().GetItem();
        } else {
            std::cerr << "Failed to get movie: " << outcome.GetError().GetMessage() << std::endl;
        }
    } catch (const Aws::DynamoDB::DynamoDBException& e) {
        std::cerr << "Error getting movie: " << e.what() << std::endl;
    }
    
    return std::map<std::string, Aws::DynamoDB::Model::AttributeValue>();
}

bool MovieRepository::Update(const std::string& title, int year, const std::string& plot, double rating) {
    Aws::DynamoDB::Model::UpdateItemRequest request;
    request.SetTableName(m_tableName);
    
    Aws::DynamoDB::Model::AttributeValue yearAttr;
    yearAttr.SetN(std::to_string(year));
    
    Aws::DynamoDB::Model::AttributeValue titleAttr;
    titleAttr.SetS(title);
    
    request.AddKey("year", yearAttr);
    request.AddKey("title", titleAttr);
    
    // Set up the update expression
    request.SetUpdateExpression("set info.rating = :r, info.plot = :p");
    
    Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue> expressionValues;
    
    Aws::DynamoDB::Model::AttributeValue rAttr;
    rAttr.SetN(std::to_string(rating));
    expressionValues[":r"] = rAttr;
    
    Aws::DynamoDB::Model::AttributeValue pAttr;
    pAttr.SetS(plot);
    expressionValues[":p"] = pAttr;
    
    request.SetExpressionAttributeValues(expressionValues);
    request.SetReturnValues(Aws::DynamoDB::Model::ReturnValue::UPDATED_NEW);
    
    try {
        auto outcome = m_dynamoDbClient->UpdateItem(request);
        if (outcome.IsSuccess()) {
            return true;
        } else {
            std::cerr << "Failed to update movie: " << outcome.GetError().GetMessage() << std::endl;
        }
    } catch (const Aws::DynamoDB::DynamoDBException& e) {
        std::cerr << "Error updating movie: " << e.what() << std::endl;
    }
    
    return false;
}

std::vector<std::map<std::string, Aws::DynamoDB::Model::AttributeValue>> MovieRepository::QueryMovies(int year) {
    std::vector<std::map<std::string, Aws::DynamoDB::Model::AttributeValue>> movies;
    
    Aws::DynamoDB::Model::QueryRequest request;
    request.SetTableName(m_tableName);
    
    // Set up the key condition expression
    request.SetKeyConditionExpression("year = :y");
    
    Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue> expressionValues;
    Aws::DynamoDB::Model::AttributeValue yAttr;
    yAttr.SetN(std::to_string(year));
    expressionValues[":y"] = yAttr;
    
    request.SetExpressionAttributeValues(expressionValues);
    
    try {
        bool moreItemsRemaining = true;
        while (moreItemsRemaining) {
            auto outcome = m_dynamoDbClient->Query(request);
            if (outcome.IsSuccess()) {
                const auto& items = outcome.GetResult().GetItems();
                for (const auto& item : items) {
                    movies.push_back(item);
                }
                
                // Check if there are more items to retrieve
                const auto& lastEvaluatedKey = outcome.GetResult().GetLastEvaluatedKey();
                if (lastEvaluatedKey.empty()) {
                    moreItemsRemaining = false;
                } else {
                    request.SetExclusiveStartKey(lastEvaluatedKey);
                }
            } else {
                std::cerr << "Failed to query movies: " << outcome.GetError().GetMessage() << std::endl;
                moreItemsRemaining = false;
            }
        }
    } catch (const Aws::DynamoDB::DynamoDBException& e) {
        std::cerr << "Error querying movies: " << e.what() << std::endl;
    }
    
    return movies;
}

std::vector<std::map<std::string, Aws::DynamoDB::Model::AttributeValue>> MovieRepository::ScanMovies(int firstYear, int secondYear) {
    std::vector<std::map<std::string, Aws::DynamoDB::Model::AttributeValue>> movies;
    
    Aws::DynamoDB::Model::ScanRequest request;
    request.SetTableName(m_tableName);
    
    // Set up the filter expression
    request.SetFilterExpression("year BETWEEN :y1 AND :y2");
    request.SetProjectionExpression("#yr, title, info.rating");
    
    Aws::Map<Aws::String, Aws::String> expressionAttributeNames;
    expressionAttributeNames["#yr"] = "year";
    request.SetExpressionAttributeNames(expressionAttributeNames);
    
    Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue> expressionValues;
    
    Aws::DynamoDB::Model::AttributeValue y1Attr;
    y1Attr.SetN(std::to_string(firstYear));
    expressionValues[":y1"] = y1Attr;
    
    Aws::DynamoDB::Model::AttributeValue y2Attr;
    y2Attr.SetN(std::to_string(secondYear));
    expressionValues[":y2"] = y2Attr;
    
    request.SetExpressionAttributeValues(expressionValues);
    
    try {
        bool moreItemsRemaining = true;
        while (moreItemsRemaining) {
            auto outcome = m_dynamoDbClient->Scan(request);
            if (outcome.IsSuccess()) {
                const auto& items = outcome.GetResult().GetItems();
                for (const auto& item : items) {
                    movies.push_back(item);
                }
                
                // Check if there are more items to retrieve
                const auto& lastEvaluatedKey = outcome.GetResult().GetLastEvaluatedKey();
                if (lastEvaluatedKey.empty()) {
                    moreItemsRemaining = false;
                } else {
                    request.SetExclusiveStartKey(lastEvaluatedKey);
                }
            } else {
                std::cerr << "Failed to scan movies: " << outcome.GetError().GetMessage() << std::endl;
                moreItemsRemaining = false;
            }
        }
    } catch (const Aws::DynamoDB::DynamoDBException& e) {
        std::cerr << "Error scanning movies: " << e.what() << std::endl;
    }
    
    return movies;
}

bool MovieRepository::Delete(const std::string& title, int year) {
    Aws::DynamoDB::Model::DeleteItemRequest request;
    request.SetTableName(m_tableName);
    
    Aws::DynamoDB::Model::AttributeValue yearAttr;
    yearAttr.SetN(std::to_string(year));
    
    Aws::DynamoDB::Model::AttributeValue titleAttr;
    titleAttr.SetS(title);
    
    request.AddKey("year", yearAttr);
    request.AddKey("title", titleAttr);
    
    try {
        auto outcome = m_dynamoDbClient->DeleteItem(request);
        if (outcome.IsSuccess()) {
            return true;
        } else {
            std::cerr << "Failed to delete movie: " << outcome.GetError().GetMessage() << std::endl;
        }
    } catch (const Aws::DynamoDB::DynamoDBException& e) {
        std::cerr << "Error deleting movie: " << e.what() << std::endl;
    }
    
    return false;
}

bool MovieRepository::DeleteTable() {
    Aws::DynamoDB::Model::DeleteTableRequest request;
    request.SetTableName(m_tableName);
    
    try {
        auto outcome = m_dynamoDbClient->DeleteTable(request);
        if (outcome.IsSuccess()) {
            m_tableName = "";
            return true;
        } else {
            std::cerr << "Failed to delete table: " << outcome.GetError().GetMessage() << std::endl;
        }
    } catch (const Aws::DynamoDB::DynamoDBException& e) {
        std::cerr << "Error deleting table: " << e.what() << std::endl;
    }
    
    return false;
}

bool MovieRepository::WriteBatch(const std::vector<std::map<std::string, Aws::DynamoDB::Model::AttributeValue>>& movies) {
    // DynamoDB limits batch writes to 25 items
    const size_t batchSize = 25;
    
    try {
        for (size_t i = 0; i < movies.size(); i += batchSize) {
            Aws::DynamoDB::Model::BatchWriteItemRequest request;
            
            Aws::Map<Aws::String, Aws::Vector<Aws::DynamoDB::Model::WriteRequest>> requestItems;
            Aws::Vector<Aws::DynamoDB::Model::WriteRequest> writeRequests;
            
            size_t end = std::min(i + batchSize, movies.size());
            for (size_t j = i; j < end; ++j) {
                Aws::DynamoDB::Model::WriteRequest writeRequest;
                Aws::DynamoDB::Model::PutRequest putRequest;
                putRequest.SetItem(movies[j]);
                writeRequest.SetPutRequest(putRequest);
                writeRequests.push_back(writeRequest);
            }
            
            requestItems[m_tableName] = writeRequests;
            request.SetRequestItems(requestItems);
            
            auto outcome = m_dynamoDbClient->BatchWriteItem(request);
            if (!outcome.IsSuccess()) {
                std::cerr << "Failed to write batch: " << outcome.GetError().GetMessage() << std::endl;
                return false;
            }
            
            // Handle unprocessed items
            auto unprocessedItems = outcome.GetResult().GetUnprocessedItems();
            while (!unprocessedItems.empty()) {
                std::this_thread::sleep_for(std::chrono::milliseconds(100));
                
                Aws::DynamoDB::Model::BatchWriteItemRequest retryRequest;
                retryRequest.SetRequestItems(unprocessedItems);
                
                outcome = m_dynamoDbClient->BatchWriteItem(retryRequest);
                if (!outcome.IsSuccess()) {
                    std::cerr << "Failed to write unprocessed items: " << outcome.GetError().GetMessage() << std::endl;
                    return false;
                }
                
                unprocessedItems = outcome.GetResult().GetUnprocessedItems();
            }
        }
        
        return true;
    } catch (const Aws::DynamoDB::DynamoDBException& e) {
        std::cerr << "Error writing batch: " << e.what() << std::endl;
    }
    
    return false;
}

} // namespace AmazonQCustomizationDemo
