#FROM golang:1.16.5 as backend-builder
FROM golang:1.23 as backend-builder

WORKDIR /workspace

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o backend-server console/backend/main.go

FROM node:12.14.1 as frontend-builder

WORKDIR /workspace

COPY console/frontend/package*.json ./
RUN npm --registry=https://registry.npmmirror.com install --no-optional

COPY console/frontend/ .
RUN npm run build

FROM alpine:latest
WORKDIR /

ARG ARG_TZ=Etc/UTC
COPY --from=frontend-builder /workspace/dist ./console/frontend/dist
COPY --from=backend-builder /workspace/backend-server ./backend-server
ENV TZ=$ARG_TZ
RUN apk add -U tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
#RUN chmod +x ./startup.sh

ENTRYPOINT ["/backend-server"]
