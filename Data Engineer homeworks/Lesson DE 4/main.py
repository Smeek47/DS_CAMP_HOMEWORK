from fastapi import FastAPI, HTTPException

app = FastAPI()

records = []

@app.post("/api/add_record/{record}")
async def add_record(record: str):
    records.append(record)
    return {"message": f"New added record: {record}"}

@app.get("/api/last_10_records")
async def last_10_records():
    last_10 = records[-10:]
    return {"Last 10 added records": last_10}

@app.delete("/api/delete_record/{record}")
async def delete_record(record: str):
    if record in records:
        records.remove(record)
        return {"message": f"Removed record: {record}"}
    else:
        raise HTTPException(status_code=404, detail=f"Record {record} not found")