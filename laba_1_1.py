{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyP8K7sCQK+1mpQZSmvqVlZq"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["import csv\n","\n","with open('books.csv', 'r', encoding='cp1251') as f:\n","     reader = csv.DictReader(f)\n","     cnt = 0\n","     for line in reader:\n","          cnt += 1\n","print(f'Кол-во записей в файле: {cnt}')\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"GqbesTcv8s2l","executionInfo":{"status":"ok","timestamp":1696360832162,"user_tz":-180,"elapsed":301,"user":{"displayName":"Полина Завьялова","userId":"03410606161305179301"}},"outputId":"796ab4ed-666d-4110-aa3a-fd5dec0792df"},"execution_count":5,"outputs":[{"output_type":"stream","name":"stdout","text":["Кол-во записей в файле: 9409\n"]}]}]}