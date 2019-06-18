import json


 
  

def lambda_handler(event, context):
    def sumOfSeries(n): 
        sum = 0
        for i in range(1, n+1):
            sum +=i*i*i 
        return sum
    n = 5
    print(sumOfSeries(n))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
