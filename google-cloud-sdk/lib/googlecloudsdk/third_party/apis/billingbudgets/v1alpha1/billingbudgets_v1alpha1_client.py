"""Generated client library for billingbudgets version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.billingbudgets.v1alpha1 import billingbudgets_v1alpha1_messages as messages


class BillingbudgetsV1alpha1(base_api.BaseApiClient):
  """Generated client library for service billingbudgets version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://billingbudgets.googleapis.com/'

  _PACKAGE = u'billingbudgets'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'BillingbudgetsV1alpha1'
  _URL_VERSION = u'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new billingbudgets handle."""
    url = url or self.BASE_URL
    super(BillingbudgetsV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.billingAccounts_budgets = self.BillingAccountsBudgetsService(self)
    self.billingAccounts = self.BillingAccountsService(self)

  class BillingAccountsBudgetsService(base_api.BaseApiService):
    """Service class for the billingAccounts_budgets resource."""

    _NAME = u'billingAccounts_budgets'

    def __init__(self, client):
      super(BillingbudgetsV1alpha1.BillingAccountsBudgetsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new budget. See.
<a href="https://cloud.google.com/billing/quotas">Quotas and limits</a>
for more information on the limits of the number of budgets you can create.

      Args:
        request: (BillingbudgetsBillingAccountsBudgetsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudBillingBudgetsV1alpha1Budget) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/billingAccounts/{billingAccountsId}/budgets',
        http_method=u'POST',
        method_id=u'billingbudgets.billingAccounts.budgets.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}/budgets',
        request_field=u'googleCloudBillingBudgetsV1alpha1CreateBudgetRequest',
        request_type_name=u'BillingbudgetsBillingAccountsBudgetsCreateRequest',
        response_type_name=u'GoogleCloudBillingBudgetsV1alpha1Budget',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a budget. Returns successfully if already deleted.

      Args:
        request: (BillingbudgetsBillingAccountsBudgetsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/billingAccounts/{billingAccountsId}/budgets/{budgetsId}',
        http_method=u'DELETE',
        method_id=u'billingbudgets.billingAccounts.budgets.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'BillingbudgetsBillingAccountsBudgetsDeleteRequest',
        response_type_name=u'GoogleProtobufEmpty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Returns a budget.

      Args:
        request: (BillingbudgetsBillingAccountsBudgetsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudBillingBudgetsV1alpha1Budget) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/billingAccounts/{billingAccountsId}/budgets/{budgetsId}',
        http_method=u'GET',
        method_id=u'billingbudgets.billingAccounts.budgets.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'BillingbudgetsBillingAccountsBudgetsGetRequest',
        response_type_name=u'GoogleCloudBillingBudgetsV1alpha1Budget',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Returns a list of budgets for a billing account.

      Args:
        request: (BillingbudgetsBillingAccountsBudgetsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudBillingBudgetsV1alpha1ListBudgetsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/billingAccounts/{billingAccountsId}/budgets',
        http_method=u'GET',
        method_id=u'billingbudgets.billingAccounts.budgets.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/budgets',
        request_field='',
        request_type_name=u'BillingbudgetsBillingAccountsBudgetsListRequest',
        response_type_name=u'GoogleCloudBillingBudgetsV1alpha1ListBudgetsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a budget and returns the updated budget.

      Args:
        request: (BillingbudgetsBillingAccountsBudgetsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudBillingBudgetsV1alpha1Budget) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/billingAccounts/{billingAccountsId}/budgets/{budgetsId}',
        http_method=u'PATCH',
        method_id=u'billingbudgets.billingAccounts.budgets.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field=u'googleCloudBillingBudgetsV1alpha1UpdateBudgetRequest',
        request_type_name=u'BillingbudgetsBillingAccountsBudgetsPatchRequest',
        response_type_name=u'GoogleCloudBillingBudgetsV1alpha1Budget',
        supports_download=False,
    )

  class BillingAccountsService(base_api.BaseApiService):
    """Service class for the billingAccounts resource."""

    _NAME = u'billingAccounts'

    def __init__(self, client):
      super(BillingbudgetsV1alpha1.BillingAccountsService, self).__init__(client)
      self._upload_configs = {
          }