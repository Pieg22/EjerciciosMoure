{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOmHt6beRzGo8U+PlTPp1jC",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Pieg22/EjerciciosMoure/blob/master/06_tuplas_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprÃ­mela.\n",
        "\n",
        "tuple_1 = (10, 20, 30, 40, 50)\n",
        "print(tuple_1)\n",
        "\n",
        "# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muÃ©stralo.\n",
        "\n",
        "tuple_2 = (100, 200, 300, 400, 500)\n",
        "print(tuple_2[2])\n",
        "\n",
        "# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.\n",
        "\n",
        "tuple_4 = (1 ,2 ,3)\n",
        "\n",
        "#tuple_4[1] = 10 Esto explota\n",
        "\n",
        "# 4. Cuenta cuÃ¡ntas veces aparece el nÃºmero 3 en la tupla (1, 2, 3, 3, 4, 5, 3).\n",
        "\n",
        "tuple_5 = (1, 2, 3, 3, 4, 5, 3)\n",
        "\n",
        "print(tuple_5.count(3))\n",
        "\n",
        "\n",
        "# 5. Encuentra el Ã­ndice de la primera apariciÃ³n de la cadena \"Python\" en la tupla (\"Java\", \"Python\", \"JavaScript\", \"Python\").\n",
        "\n",
        "tuple_6 = (\"Java\", \"Python\", \"Javascript\", \"Python\")\n",
        "\n",
        "print(tuple_6.index(\"Python\"))\n",
        "\n",
        "# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.\n",
        "\n",
        "tuple_7 = (1, 2, 3)\n",
        "tuple_8 = (4, 5, 6)\n",
        "\n",
        "sum_tuple= (tuple_7 + tuple_8)\n",
        "print(sum_tuple)\n",
        "\n",
        "# 7. Crea una subtupla con los elementos desde la posiciÃ³n 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).\n",
        "\n",
        "sub_tuple = tuple_1[2:4]\n",
        "print(sub_tuple)\n",
        "\n",
        "# 8. Convierte la tupla (\"rojo\", \"verde\", \"azul\") en una lista, cambia el segundo elemento a \"amarillo\" y vuelve a convertirla en una tupla. Imprime la tupla resultante.\n",
        "tuple_color = (\"rojo\" , \"verde\" , \"azul\")\n",
        "\n",
        "tuple_color = list(tuple_color) #convert tuple to list\n",
        "\n",
        "tuple_color.remove(\"azul\") #remove the second position\n",
        "tuple_color.insert( 2, \"Amarillo\") #adding the \"yellow\" on the second position\n",
        "\n",
        "tuple_color = tuple(tuple_color)\n",
        "\n",
        "print(tuple_color)\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JTeIMVjYzgGf",
        "outputId": "b5c091cc-6c99-4090-9a14-073d466e097c"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(10, 20, 30, 40, 50)\n",
            "300\n",
            "3\n",
            "1\n",
            "(1, 2, 3, 4, 5, 6)\n",
            "(30, 40)\n",
            "<class 'tuple'>\n"
          ]
        }
      ]
    }
  ]
}