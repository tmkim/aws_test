from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import os
from django.core.files.storage import default_storage

import logging

logger = logging.getLogger(__name__)

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file uploaded'}, status=400)

        # Log storage backend being used
        logger.info(f"Storage backend: {type(default_storage)}")
        print(f"Storage backend: {type(default_storage)}")
        
        # Save the file to the storage backend (S3 or local)
        file_path = default_storage.save(f"uploads/{file.name}", file)
        logger.info(f"File saved to: {file_path}")
        print(f"File saved to: {file_path}")

        # Construct the file URL
        file_url = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{file_path}"

        return Response({'url': file_url})