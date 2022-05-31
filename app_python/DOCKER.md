# Best pratices

- Run the container with non-root user
- Single app inside the container
- Distroless images and trusted base images
- Only port 5000 is exposed by the container
- Use COPY instructions instead of ADD when possible
- Use of CMD instead of the ENTRYPOINT
- Use Linter on Dockerfile to detect bad practice [hadolint](https://github.com/hadolint/hadolint)