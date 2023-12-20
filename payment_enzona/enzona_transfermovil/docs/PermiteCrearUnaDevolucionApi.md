# enzona_transfermovil.PermiteCrearUnaDevolucionApi

All URIs are relative to *https://api.enzona.net/transfermovil/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_transaction_uuid_refunds_post**](PermiteCrearUnaDevolucionApi.md#payments_transaction_uuid_refunds_post) | **POST** /payments/{transaction_uuid}/refunds | 


# **payments_transaction_uuid_refunds_post**
> PaymentsPost200Response payments_transaction_uuid_refunds_post(transaction_uuid, payload=payload)



### Example

```python
import time
import os
import enzona_transfermovil
from enzona_transfermovil.models.payments_post200_response import PaymentsPost200Response
from enzona_transfermovil.models.payments_transaction_uuid_refunds_post_request import PaymentsTransactionUuidRefundsPostRequest
from enzona_transfermovil.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.enzona.net/transfermovil/v1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = enzona_transfermovil.Configuration(
    host = "https://api.enzona.net/transfermovil/v1.0.0"
)


# Enter a context with an instance of the API client
with enzona_transfermovil.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enzona_transfermovil.PermiteCrearUnaDevolucionApi(api_client)
    transaction_uuid = 'transaction_uuid_example' # str | 
    payload = enzona_transfermovil.PaymentsTransactionUuidRefundsPostRequest() # PaymentsTransactionUuidRefundsPostRequest | Parámetros de entrada (optional)

    try:
        api_response = api_instance.payments_transaction_uuid_refunds_post(transaction_uuid, payload=payload)
        print("The response of PermiteCrearUnaDevolucionApi->payments_transaction_uuid_refunds_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermiteCrearUnaDevolucionApi->payments_transaction_uuid_refunds_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_uuid** | **str**|  | 
 **payload** | [**PaymentsTransactionUuidRefundsPostRequest**](PaymentsTransactionUuidRefundsPostRequest.md)| Parámetros de entrada | [optional] 

### Return type

[**PaymentsPost200Response**](PaymentsPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pago creado correctamente. |  -  |
**400** | Sintaxis inválida en la petición. |  -  |
**401** | No autenticado. |  -  |
**403** | Permisos insuficientes para acceder a este contenido. |  -  |
**404** | El servidor no pudo encontrar el contenido solicitado. |  -  |
**429** | Se ha sobrepasado el límite de las solicitudes en un período de tiempo dado. |  -  |
**500** | Error interno en el servidor. |  -  |
**503** | El servidor no esta listo para manejar la petición. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

