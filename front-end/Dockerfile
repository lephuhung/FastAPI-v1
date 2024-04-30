# Use the official lightweight Node.js 14 image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the local code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 3011

# Command to run the application
CMD ["npm", "start"]