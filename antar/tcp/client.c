#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080

int main() {
  int sock = 0;
  struct sockaddr_in serv_addr;
  char buffer[1024] = {0};

  // Have the end user input a message that
  // they want to send to the server side.
  const char *message = "Hello from client";

  // Creating socket
  if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
    perror("Socket creation error");
    return -1;
  }

  serv_addr.sin_family = AF_INET;
  serv_addr.sin_port = htons(PORT);

  // Converting IPv4 and IPv6 addresses from text to binary form.
  if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
    perror("Invalid address/ Address not supported");
    return -1;
  }

  // Connecting to server
  if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
    perror("Connection Failed");
    return -1;
  }

  // Sending message to server
  send(sock, message, strlen(message), 0);
  printf("Message sent\n");

  // Reading server response
  read(sock, buffer, 1024);
  printf("Received from server: %s\n", buffer);

  close(sock);
  return 0;
}