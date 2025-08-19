/* Include the necessary libraries that allow
   the program to perform input/output, memory
   management, string operations, POSIX API
   (unistd.h), and socket functions (arpa/inet.h). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

// Sets the port number on which the server
// will listen for incoming connections.
#define PORT 8080

int main() {
  // server_fd: File descriptor for the server socket.
  // new_socket: File descriptor returned by the
  // accept() function.

  /* Comprehending the difference:

     // 1. Create a server socket that listens.
     server_fd = socket(...);

     // 2. Put server_fd (socket file descriptor) into
     //    listening mode.
     listen(server_fd, ...);

     // 3. Accept a client connection.
     new_socket = accept(server_fd, ...);

     You listen with server_fd, but once a client
     connects, you communicate with them through
     new_socket.
  */
  int server_fd, new_socket;

  /* struct sockaddr_in is a structure used to
     define an IPv4 address and port number.

     This structure tells the OS where your server
     will listen (IP and port).
  */
  struct sockaddr_in address;

  // addr_len: Size of the address structure.
  int addr_len = sizeof(address);

  // buffer: Buffer for reading incoming data.
  char buffer[1024] = {0};

  // hello: Message to send back to the client.
  const char *hello = "Hello from server";

  // 1. Creating socket file descriptor
  if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
    perror("Socket failed");
    exit(EXIT_FAILURE);
  }

  /*
  sockaddr_in has these key members:
  sin_family: address family (e.g., AF_INET for IPv4)

  sin_addr.s_addr: the IP address (e.g., INADDR_ANY for "all interfaces")

  sin_port: the port number (e.g., 8080, but passed using htons())

  Source:
  https://learn.microsoft.com/en-us/windows/win32/api/ws2def/ns-ws2def-sockaddr_in
  */

  // Binding the socket to the port
  address.sin_family = AF_INET;

  // sin_addr is a struct (IN_ADDR).
  // https://learn.microsoft.com/en-us/windows/win32/api/ws2def/ns-ws2def-sockaddr_in

  // s_addr is a field inside that struct.
  // https://learn.microsoft.com/en-us/windows/win32/api/winsock2/ns-winsock2-in_addr
  address.sin_addr.s_addr = INADDR_ANY;

  /* htons() stands for "Host To Network Short".
     It converts a 16-bit (short) integer from
     host byte order to network byte order. */

  // A transport protocol port number.
  address.sin_port = htons(PORT);

  if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
    perror("Bind failed");
    close(server_fd);
    exit(EXIT_FAILURE);
  }

  // 2. Listening for incoming connections
  if (listen(server_fd, 3) < 0) {
    perror("Listen failed");
    close(server_fd);
    exit(EXIT_FAILURE);
  }

  printf("Waiting for a connection...\n");
  // 3. Returns a file descriptor.
  if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addr_len)) < 0) {
    perror("Accept failed");
    close(server_fd);
    exit(EXIT_FAILURE);
  }

  // Reading message from the client
  ssize_t bytes_read = read(new_socket, buffer, 1024);

  if (bytes_read < 0) {
    perror("read failed");
  } else if (bytes_read == 0) {
    printf("Client disconnected\n");
  } else {
    printf("Read %zd bytes: %s\n", bytes_read, buffer);
  }

  // Sending response
  ssize_t bytes_sent = send(new_socket, hello, strlen(hello), 0);

  if (bytes_sent == -1) {
    perror("send failed");
    exit(EXIT_FAILURE);
  } else {
    printf("Hello message sent\n");
  }

  close(new_socket);
  close(server_fd);

  return 0;
}