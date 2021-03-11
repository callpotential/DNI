from aws_cdk import (core,
                     aws_apigateway as apigateway,
                     aws_lambda as lambda_)
from aws_cdk.aws_apigateway import IntegrationResponse


class WidgetService(core.Construct):
    def __init__(self, scope: core.Construct, id: str):
        super().__init__(scope, id)

        handler = lambda_.Function(self, "dni_test_cdk",
                    runtime=lambda_.Runtime.PYTHON_3_6,
                    code=lambda_.Code.from_asset("resources"),
                    handler="call_start_service.handler")

        api = apigateway.RestApi(self, "widgets-api",
                  rest_api_name="Widget Service",
                  description="This service serves widgets.")

        get_widgets_integration = apigateway.LambdaIntegration(handler,
                request_templates={"application/x-www-form-urlencoded": """#set($httpPost = $input.path('$').split("&"))
{
#foreach( $kvPair in $httpPost )
 #set($kvTokenised = $kvPair.split("="))
 #if( $kvTokenised.size() > 1 )
   "$kvTokenised[0]" : "$kvTokenised[1]"#if( $foreach.hasNext ),#end
 #else
   "$kvTokenised[0]" : ""#if( $foreach.hasNext ),#end
 #end
#end
}"""},
                integration_responses=[
                    IntegrationResponse(
                        status_code="200",
                        response_templates={"application/xml": "#set($inputRoot = $input.path('$'))$inputRoot.body"}
                    )
                ])

        api.root.add_method("GET", get_widgets_integration)   # GET /