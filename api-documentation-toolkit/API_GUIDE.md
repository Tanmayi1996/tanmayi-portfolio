# Atlas Tasks API guide

> Portfolio sample only. `api.example.com` is a reserved example hostname; this is not a live API.

## Overview
The Atlas Tasks API is a fictional REST API for creating and retrieving tasks. The base URL is `https://api.example.com/v1`. Requests and responses use JSON.

## Authentication
This sample describes an authenticated API but intentionally does not prescribe a real authentication mechanism. In production, document the supported scheme, token acquisition, scopes, and credential rotation process.

## List tasks
`GET /tasks`

Returns tasks visible to the authenticated user.

| Parameter | In | Required | Description |
|---|---|---:|---|
| `status` | query | No | Filter by `open` or `completed`. |
| `limit` | query | No | Maximum number of results (1–100; default 20). |

Example response:
```json
{"items":[{"id":"task_123","title":"Review onboarding guide","status":"open"}],"count":1}
```

## Create a task
`POST /tasks`

Send a JSON body with a required `title` and optional `description`.
```json
{"title":"Review onboarding guide","description":"Check links and screenshots."}
```
A successful request returns `201 Created`. A `400` response indicates request validation failed; `401` indicates missing or invalid authentication.

## Get a task
`GET /tasks/{taskId}`

Replace `{taskId}` with the task identifier. A `404` response means no task matches the supplied ID.

## Error handling
| Status | Meaning | Suggested action |
|---|---|---|
| `400` | Request validation failed | Check required fields and value constraints. |
| `401` | Authentication missing or invalid | Check configured credentials. |
| `404` | Task not found | Verify the task ID. |

Keep this guide and the OpenAPI contract aligned as the API evolves.