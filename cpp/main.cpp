#include <iostream>
#include "Generator.h"

int main() {
    // Initialize the AWS SDK
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    
    {
        AmazonQCustomizationDemo::Generator generator;
        if (!generator.GenerateFromCsv("movies.csv")) {
            std::cerr << "Failed to generate examples from CSV" << std::endl;
            Aws::ShutdownAPI(options);
            return 1;
        }
    }
    
    // Shutdown the AWS SDK
    Aws::ShutdownAPI(options);
    return 0;
}
