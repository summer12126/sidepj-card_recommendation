import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
import sys

def test_elasticsearch_connection():
    # Load environment variables
    load_dotenv()
    
    # Get credentials
    user = os.getenv('ELASTIC_USER')
    passwd = os.getenv('ELASTIC_PASSWD')
    
    print(f"Testing Elasticsearch connection...")
    print(f"Username being used: {user}")
    print(f"Password length: {'*' * len(passwd) if passwd else 'No password found'}")
    
    try:
        # Initialize Elasticsearch client
        es = Elasticsearch(
            'https://localhost:9200',
            basic_auth=(user, passwd),
            verify_certs=False,
            ssl_show_warn=False
        )
        
        # Test connection
        if es.ping():
            print("Successfully connected to Elasticsearch!")
            
            # List all indices
            indices = es.indices.get_alias().keys()
            print("\nAvailable indices:")
            for index in indices:
                print(f"- {index}")
            
            # Test specific index
            if 'df_credit' in indices:
                # Get mapping for df_credit
                mapping = es.indices.get_mapping(index='df_credit')
                print("\ndf_credit mapping:")
                print(mapping)
                
                # Get a sample document
                try:
                    sample = es.search(index='df_credit', size=1)
                    print("\nSample document:")
                    print(sample['hits']['hits'][0]['_source'])
                except Exception as e:
                    print(f"\nError getting sample document: {str(e)}")
            else:
                print("\nWarning: df_credit index not found!")
                
        else:
            print("Failed to connect! Server is not responding to ping.")
            
    except Exception as e:
        print(f"\nConnection Error: {str(e)}")
        print("\nTroubleshooting steps:")
        print("1. Verify your credentials in .env file")
        print("2. Check if Elasticsearch is running:")
        print("   - curl -XGET 'https://localhost:9200' -u 'elastic:your_password'")
        print("3. Verify the elastic user password:")
        print("   - If you need to reset it, use:")
        print("   - /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic")
        
if __name__ == "__main__":
    test_elasticsearch_connection()