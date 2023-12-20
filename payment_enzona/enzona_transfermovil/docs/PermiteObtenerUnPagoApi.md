# enzona_transfermovil.PermiteObtenerUnPagoApi

All URIs are relative to *https://api.enzona.net/transfermovil/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_merchant_op_id_get**](PermiteObtenerUnPagoApi.md#payments_merchant_op_id_get) | **GET** /payments/{merchant_op_id} | 


# **payments_merchant_op_id_get**
> payments_merchant_op_id_get(merchant_op_id)



### Example

```python
import time
import os
import enzona_transfermovil
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
    api_instance = enzona_transfermovil.PermiteObtenerUnPagoApi(api_client)
    merchant_op_id = 'merchant_op_id_example' # str | 

    try:
        api_instance.payments_merchant_op_id_get(merchant_op_id)
    except Exception as e:
        print("Exception when calling PermiteObtenerUnPagoApi->payments_merchant_op_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_op_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Listado de pagos. |  -  |
**400** | Sintaxis inválida en la petición. |  -  |
**401** | No autenticado. |  -  |
**403** | Permisos insuficientes para acceder a este contenido. |  -  |
**404** | El servidor no pudo encontrar el contenido solicitado. |  -  |
**429** | Se ha sobrepasado el límite de las solicitudes en un período de tiempo dado. |  -  |
**500** | Error interno en el servidor. |  -  |
**503** | El servidor no esta listo para manejar la petición. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

