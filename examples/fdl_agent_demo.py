from fdl_kernel import FDLAgent

agent = FDLAgent(context="Пример: размышление о силе и порядке")

input_query = "Решения силой — единственный путь к порядку."
response = agent.respond(input_query)

print("Запрос:", input_query)
print("Ответ агента:", response)
