from django.db import models

class Calculation(models.Model):
    expression = models.CharField(max_length=255, verbose_name="Expressão")
    result = models.CharField(max_length=255, verbose_name="Resultado")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Data/Hora")

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Cálculo"
        verbose_name_plural = "Cálculos"

    def __str__(self):
        return f"{self.expression} = {self.result}"
