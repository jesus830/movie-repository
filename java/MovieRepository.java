package com.amazonaws.demo;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.*;
import com.amazonaws.services.dynamodbv2.document.spec.*;
import com.amazonaws.services.dynamodbv2.document.utils.ValueMap;
import com.amazonaws.services.dynamodbv2.model.*;
import com.amazonaws.services.dynamodbv2.document.internal.IteratorSupport;

import java.math.BigDecimal;
import java.util.*;
import java.util.concurrent.TimeUnit;

/**
 * Encapsulates an Amazon DynamoDB table of movie data.
 */
public class MovieRepository {
    private final AmazonDynamoDB dynamoDbClient;
    private final DynamoDB dynamoDB;
    private Table table;
    private final String tableName;

    /**
     * Constructor for MovieRepository.
     * 
     * @param dynamoDbClient A DynamoDB client. If null, a new client will be created.
     * @param tableName The name of the table. Defaults to "Movies".
     */
    public MovieRepository(AmazonDynamoDB dynamoDbClient, String tableName) {
        this.dynamoDbClient = dynamoDbClient != null ? dynamoDbClient : AmazonDynamoDBClientBuilder.standard().build();
        this.dynamoDB = new DynamoDB(this.dynamoDbClient);
        this.tableName = tableName != null ? tableName : "Movies";
        
        // Check if the table exists
        if (exists(this.tableName)) {
            this.table = dynamoDB.getTable(this.tableName);
        }
    }

    /**
     * Constructor with default table name.
     * 
     * @param dynamoDbClient A DynamoDB client.
     */
    public MovieRepository(AmazonDynamoDB dynamoDbClient) {
        this(dynamoDbClient, "Movies");
    }

    /**
     * Default constructor.
     */
    public MovieRepository() {
        this(null, "Movies");
    }

    /**
     * Determines whether a table exists.
     * 
     * @param tableName The name of the table to check.
     * @return True when the table exists; otherwise, False.
     */
    public boolean exists(String tableName) {
        try {
            table = dynamoDB.getTable(tableName);
            table.describe();
            return true;
        } catch (ResourceNotFoundException e) {
            return false;
        } catch (Exception e) {
            System.err.println("Error checking if table exists: " + e.getMessage());
            throw e;
        }
    }

    /**
     * Creates an Amazon DynamoDB table that can be used to store movie data.
     * 
     * @param tableName The name of the table to create.
     * @return The newly created table.
     */
    public Table createTable(String tableName) {
        try {
            List<KeySchemaElement> keySchema = new ArrayList<>();
            keySchema.add(new KeySchemaElement().withAttributeName("year").withKeyType(KeyType.HASH)); // Partition key
            keySchema.add(new KeySchemaElement().withAttributeName("title").withKeyType(KeyType.RANGE)); // Sort key

            List<AttributeDefinition> attributeDefinitions = new ArrayList<>();
            attributeDefinitions.add(new AttributeDefinition().withAttributeName("year").withAttributeType("N"));
            attributeDefinitions.add(new AttributeDefinition().withAttributeName("title").withAttributeType("S"));

            ProvisionedThroughput provisionedThroughput = new ProvisionedThroughput()
                .withReadCapacityUnits(10L)
                .withWriteCapacityUnits(10L);

            CreateTableRequest request = new CreateTableRequest()
                .withTableName(tableName)
                .withKeySchema(keySchema)
                .withAttributeDefinitions(attributeDefinitions)
                .withProvisionedThroughput(provisionedThroughput);

            table = dynamoDB.createTable(request);
            
            // Wait for the table to become active
            table.waitForActive();
            
            return table;
        } catch (Exception e) {
            System.err.println("Couldn't create table " + tableName + ". Error: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }

    /**
     * Lists the Amazon DynamoDB tables for the current account.
     * 
     * @return The list of tables.
     */
    public List<String> listTables() {
        try {
            List<String> tableNames = new ArrayList<>();
            TableCollection<ListTablesResult> tables = dynamoDB.listTables();
            Iterator<Table> iterator = tables.iterator();
            
            while (iterator.hasNext()) {
                Table table = iterator.next();
                String tableName = table.getTableName();
                System.out.println(tableName);
                tableNames.add(tableName);
            }
            
            return tableNames;
        } catch (Exception e) {
            System.err.println("Couldn't list tables. Error: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }

    /**
     * Adds a movie to the table.
     * 
     * @param title The title of the movie.
     * @param year The release year of the movie.
     * @param plot The plot summary of the movie.
     * @param rating The quality rating of the movie.
     */
    public void insert(String title, int year, String plot, BigDecimal rating) {
        try {
            Item item = new Item()
                .withPrimaryKey("year", year, "title", title)
                .withMap("info", new HashMap<String, Object>() {{
                    put("plot", plot);
                    put("rating", rating);
                }});

            table.putItem(item);
        } catch (Exception e) {
            System.err.println("Couldn't add movie " + title + " to table " + tableName + ". Error: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }

    /**
     * Gets movie data from the table for a specific movie.
     * 
     * @param title The title of the movie.
     * @param year The release year of the movie.
     * @return The data about the requested movie.
     */
    public Item select(String title, int year) {
        try {
            return table.getItem("year", year, "title", title);
        } catch (Exception e) {
            System.err.println("Couldn't get movie " + title + " from table " + tableName + ". Error: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }

    /**
     * Updates rating and plot data for a movie in the table.
     * 
     * @param title The title of the movie to update.
     * @param year The release year of the movie to update.
     * @param plot The updated plot summary to give the movie.
     * @param rating The updated rating to the give the movie.
     * @return The fields that were updated, with their new values.
     */
    public Document update(String title, int year, String plot, BigDecimal rating) {
        try {
            UpdateItemSpec updateItemSpec = new UpdateItemSpec()
                .withPrimaryKey("year", year, "title", title)
                .withUpdateExpression("set info.rating = :r, info.plot = :p")
                .withValueMap(new ValueMap()
                    .withNumber(":r", rating)
                    .withString(":p", plot))
                .withReturnValues(ReturnValue.UPDATED_NEW);

            return table.updateItem(updateItemSpec).getItem();
        } catch (Exception e) {
            System.err.println("Couldn't update movie " + title + " in table " + tableName + ". Error: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }

    /**
     * Queries for movies that were released in the specified year.
     * 
     * @param year The year to query.
     * @return The list of movies that were released in the specified year.
     */
    public List<Item> queryMovies(int year) {
        try {
            QuerySpec querySpec = new QuerySpec()
                .withKeyConditionExpression("year = :yyyy")
                .withValueMap(new ValueMap().withNumber(":yyyy", year));

            ItemCollection<QueryOutcome> items = table.query(querySpec);
            List<Item> results = new ArrayList<>();
            
            for (Item item : items) {
                results.add(item);
            }
            
            return results;
        } catch (Exception e) {
            System.err.println("Couldn't query for movies released in " + year + ". Error: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }

    /**
     * Scans for movies that were released in a range of years.
     * 
     * @param firstYear The first year in the range.
     * @param secondYear The second year in the range.
     * @return The list of movies released in the specified years.
     */
    public List<Item> scanMovies(int firstYear, int secondYear) {
        try {
            ScanSpec scanSpec = new ScanSpec()
                .withFilterExpression("year between :start_yr and :end_yr")
                .withValueMap(new ValueMap()
                    .withNumber(":start_yr", firstYear)
                    .withNumber(":end_yr", secondYear))
                .withProjectionExpression("year, title, info.rating");

            ItemCollection<ScanOutcome> items = table.scan(scanSpec);
            List<Item> results = new ArrayList<>();
            
            for (Item item : items) {
                results.add(item);
            }
            
            return results;
        } catch (Exception e) {
            System.err.println("Couldn't scan for movies. Error: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }

    /**
     * Deletes a movie from the table.
     * 
     * @param title The title of the movie to delete.
     * @param year The release year of the movie to delete.
     */
    public void delete(String title, int year) {
        try {
            table.deleteItem("year", year, "title", title);
        } catch (Exception e) {
            System.err.println("Couldn't delete movie " + title + ". Error: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }

    /**
     * Deletes the table.
     */
    public void deleteTable() {
        try {
            table.delete();
            table = null;
            
            // Wait for the table to be deleted
            boolean tableExists = true;
            while (tableExists) {
                try {
                    Table t = dynamoDB.getTable(tableName);
                    t.describe();
                    TimeUnit.SECONDS.sleep(1);
                } catch (ResourceNotFoundException e) {
                    tableExists = false;
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        } catch (Exception e) {
            System.err.println("Couldn't delete table. Error: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }

    /**
     * Writes a batch of movies to the table.
     * 
     * @param movies The list of movies to write.
     */
    public void writeBatch(List<Item> movies) {
        try {
            TableWriteItems tableWriteItems = new TableWriteItems(tableName);
            
            // Add each movie to the write batch
            for (Item movie : movies) {
                tableWriteItems.addItemToPut(movie);
                
                // DynamoDB has a limit of 25 items per batch
                if (tableWriteItems.getItemsToPut().size() == 25) {
                    BatchWriteItemOutcome outcome = dynamoDB.batchWriteItem(tableWriteItems);
                    
                    // Process any unprocessed items
                    while (outcome.getUnprocessedItems().size() > 0) {
                        outcome = dynamoDB.batchWriteItemUnprocessed(outcome.getUnprocessedItems());
                    }
                    
                    tableWriteItems = new TableWriteItems(tableName);
                }
            }
            
            // Write any remaining items
            if (tableWriteItems.getItemsToPut().size() > 0) {
                BatchWriteItemOutcome outcome = dynamoDB.batchWriteItem(tableWriteItems);
                
                // Process any unprocessed items
                while (outcome.getUnprocessedItems().size() > 0) {
                    outcome = dynamoDB.batchWriteItemUnprocessed(outcome.getUnprocessedItems());
                }
            }
        } catch (Exception e) {
            System.err.println("Couldn't load data into table " + tableName + ". Error: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }
}
