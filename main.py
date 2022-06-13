from fastapi import FastAPI
import numpy as np

app = FastAPI()
numbers = []

@app.get("/")
async def showMessage():
    return {"response": "this is the root. Nothing else"}

@app.get("/numbers")
async def getNumbers():
    return numbers

@app.post("/numbers")
async def addNumber(new: int):
    if isinstance(new, int) == True:
        numbers.append(new)
        result = True
        message = f"Successfully added: {new}."
        return { "message" : message ,
            "Numbers: " : numbers }
    else:
     return { "error:": "type integer number"}

@app.get("/numbers/average")
async def averageNum():
    if len(numbers) > 1:
        return { "result": f"{sum(numbers)/len(numbers)}" }
    else:
        return { "result": "Not enough number to compute.Add more numbers" }

@app.get("/numbers/sum")
async def sumNumbers():
    if len(numbers) > 1:
            return { "result": f"{sum(numbers)}" }
    else:
        return { "result": "Not enough number to compute.Add more numbers" }

@app.get("/numbers/stddev")
async def stddevNum():
    if len(numbers) > 1:
            return { "result": f"{np.std(numbers)}" }
    else:
        return { "result": "Not enough number to compute.Add more numbers" }



#dd
