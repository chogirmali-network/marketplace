import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.aws.storage import MediaStorage


class FileUploadView(APIView):
    def post(self, request, **kwargs):
        file_obj = request.data.get('file', '')

        file_directory_within_bucket = 'user_upload_files/{username}'.format(username=request.user)

        file_path_within_bucket = os.path.join(
            file_directory_within_bucket,
            file_obj.name
        )

        media_storage = MediaStorage()

        if not media_storage.exists(file_path_within_bucket):
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)

            return Response({
                'message': 'OK',
                'fileUrl': file_url,
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                'message': 'Error: file {filename} already exists at {file_directory} in bucket {bucket_name}'.format(
                    filename=file_obj.name,
                    file_directory=file_directory_within_bucket,
                    bucket_name=media_storage.bucket_name
                ),
            }, status.HTTP_400_BAD_REQUEST)
