# Use the official lightweight Node.js 14 image
FROM node:21.7-alpine3.18

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json /app
# Add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH
# Install dependencies
RUN npm install --legacy-peer-deps

# Copy the local code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 3011

# Command to run the application
CMD ["top", "-b"]