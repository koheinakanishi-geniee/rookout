from rook.serverless import serverless_rook

@serverless_rook
def lambda_handler(event, context):
    a = 8
    b = "こんにちわ"
    print(a)
    return "hello"

