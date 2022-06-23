from main import utils as main_utils
from rest_framework.views import APIView


class UploadDocumentView(APIView):
    def post(self, request):
        return main_utils.create_response({}, 200)


class DownloadDocumentView(APIView):
    def get(self, request):
        return main_utils.create_response({}, 200)


class DocumentListView(APIView):
    def get(self, request):
        return main_utils.create_response({}, 200)
