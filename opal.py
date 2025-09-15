
from opal_security.rest import ApiException
from pprint import pprint

## Defining the host is optional and defaults to https://api.opal.dev/v1
## See configuration.py for a list of all supported configuration parameters.
import opal_security as opal

configuration = opal.Configuration(
    host = "https://api.opal.dev/v1" # Replace with self-hosted domain (e.g. https://opal.example.com/v1)
)

## The client must configure the authentication and authorization parameters
## in accordance with the API server security policy.
## Examples for each auth method are provided below, use the example that
## satisfies your auth use case.

## Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = "ACCESS_TOKEN_HERE" # Opal Access Token here NOTE: can not be a read-only token
)


## Enter a context with an instance of the API client
with opal.ApiClient(configuration) as api_client:
    ## Create an instance of the API class for resources
    resources_api = opal.ResourcesApi(api_client)

    ##Create an instance of the API class for 

    # # add a resource_type_filter
    resource_type_filter = "AWS_SSO_PERMISSION_SET"

    try:
        api_response = resources_api.get_resources(resource_type_filter=resource_type_filter)
        results = api_response.results
        print("The response of ResourcesApi->get_resources:\n")
        ## pprint all results
        # pprint(results)
        for result in results:
            ## get resource users
            resource_users_response = resources_api.get_resource_users(result.resource_id)
            ## store the user list
            resource_users = resource_users_response.results
            if resource_users == []:
                resources_api.delete_resource(result.resource_id)
                pprint(result.name + " DELETED")            
    except Exception as e:
        print("Exception when calling ResourcesApi->get_resources: %s\n" % e)

