# Use the official Node-RED base image
FROM nodered/node-red:4.0.5-22

# Install additional Node-RED nodes (e.g., dashboard for UI)
RUN npm install node-red-dashboard

COPY flows.json /data/flows.json

# Expose the default Node-RED port
EXPOSE 1880

CMD ["npm", "start"]
