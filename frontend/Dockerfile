# 1. Build stage
FROM node:20-alpine AS builder

WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm

# Copy package files
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install

# Copy rest of project files
COPY . .

# Build Next.js
RUN pnpm build

# 2. Production stage
FROM node:20-alpine

WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

# Copy compiled output from builder
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY package.json pnpm-lock.yaml ./

# Install only production dependencies
RUN pnpm install --prod

EXPOSE 3000

CMD ["pnpm", "start"]
