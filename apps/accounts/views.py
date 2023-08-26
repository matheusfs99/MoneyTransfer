from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import AccountSerializer, TransactionHistorySerializer
from .models import Account, TransactionHistory
from apps.users.models import Profile


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Account.objects.all()

    @action(detail=True, methods=["post"], url_path="do-transaction")
    def do_transaction(self, request, pk):
        """
        arg:
            pk(int) -> id da conta que está efetuando o pagamento
        payload:
            value(float) -> valor da transacao
            to(int) -> id do usuário que deve receber
        """
        account = self.get_object()
        if account.profile.type == Profile.Type.SHOPKEPPER:
            return Response(
                {"error": "user of type 'lojista' cannot receive transaction"},
                status=status.HTTP_400_BAD_REQUEST
            )
        value = request.data["value"]
        if account.balance < value:
            return Response(
                {"error": "insufficient balance"},
                status=status.HTTP_400_BAD_REQUEST
            )

        receiver = self.queryset.filter(profile=request.data["to"]).first()
        if not receiver:
            return Response(
                {"error": "invalid id in field 'to'"},
                status=status.HTTP_400_BAD_REQUEST
            )

        account.balance -= value
        account.save()

        receiver.balance += value
        receiver.save()

        # transaction = TransactionHistory(
        #     value=value,
        #     payer=account.profile.user.first_name,
        #     receiver=receiver.profile.user.first_name
        # )
        # print(transaction)
        transaction = {"value": value, "payer": account.profile.user.username, "receiver": receiver.profile.user.username}
        transaction_serializer = TransactionHistorySerializer(data=transaction)
        if transaction_serializer.is_valid():
            transaction_serializer.create(transaction)
            return Response(transaction)

        return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TransactionHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = TransactionHistory.objects.all()
