# Dockerfile
FROM golang:1.22 as build
WORKDIR /src
COPY cmd/frontend/go.mod go.sum ./
RUN go mod download
COPY cmd/frontend .
RUN CGO_ENABLED=0 go build -o /bin/frontend ./cmd/frontend

FROM gcr.io/distroless/base-debian12
COPY --from=build /bin/frontend /bin/frontend
EXPOSE 8080
ENTRYPOINT ["/bin/frontend"]
