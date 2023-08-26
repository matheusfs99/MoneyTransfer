from django.db import models


class Account(models.Model):
    balance = models.FloatField("saldo", default=0)
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)


class TransactionHistory(models.Model):
    value = models.FloatField("valor", editable=False)
    payer = models.CharField("pagador", max_length=255, editable=False)
    receiver = models.CharField("recebedor", max_length=255, editable=False)
    datetime = models.DateTimeField("data e hora da transação", auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = "Transactions History"
