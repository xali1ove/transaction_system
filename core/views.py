from rest_framework.decorators import action
from .serializers import ClientSerializer
from .models import Client
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from django.db import transaction


class ClientViewSet(viewsets.ModelViewSet):
    ACTION_ALLOWS_ANY = ['register']
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self):
        if self.action in self.ACTION_ALLOWS_ANY:
            return [permissions.AllowAny()]
        return super().get_permissions()

    @transaction.atomic()
    @action(methods=["POST"], detail=True)
    def change_balance(self, request, pk):
        change_balance_value = request.data.get('change_balance_value')

        if not change_balance_value:
            return Response({"error": "`change_balance_value` is required"}, status=400)
        try:
            change_balance_value = float(change_balance_value)
        except ValueError:
            return Response({"error": "`change_balance_value` is not float type"}, status=400)

        instance: Client = self.get_object()
        if float(change_balance_value) == 0:
            return Response(
                {"message": f"Balance not changed in Client {instance.get_username()}"},
                status=200
            )
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(
            {"message": f"Updated balance to {instance.balance_value} in Client {instance.get_username()}"},
            status=200
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=["POST"], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client: Client = serializer.save()
        return Response({'message': f'Client {client.username} successfully registered.'}, status=201)


