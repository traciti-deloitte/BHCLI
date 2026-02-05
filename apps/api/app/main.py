from fastapi import FastAPI

from app.routers import (
    ai,
    analysis_runs,
    auth,
    cities,
    claims,
    cohorts,
    dashboards,
    evidence,
    graph,
    people,
    reports,
    search,
    storyboards,
    toc,
    topics,
)

app = FastAPI(title="BHCLI Impact OS API", version="0.1.0")

app.include_router(auth.router, tags=["auth"])
app.include_router(cities.router, tags=["cities"])
app.include_router(people.router, tags=["people"])
app.include_router(cohorts.router, tags=["cohorts"])
app.include_router(topics.router, tags=["topics"])
app.include_router(evidence.router, tags=["evidence"])
app.include_router(toc.router, tags=["toc"])
app.include_router(claims.router, tags=["claims"])
app.include_router(storyboards.router, tags=["storyboards"])
app.include_router(reports.router, tags=["reports"])
app.include_router(analysis_runs.router, tags=["analysis_runs"])
app.include_router(dashboards.router, tags=["dashboards"])
app.include_router(search.router, tags=["search"])
app.include_router(graph.router, tags=["graph"])
app.include_router(ai.router, tags=["ai"])


@app.get("/")
def root():
    return {"status": "ok", "service": "BHCLI Impact OS API"}
