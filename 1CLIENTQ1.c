#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main() {
    int sockfd, portno = 12345;
    struct sockaddr_in serv_addr;

    // create socket
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        perror("Error opening socket");
        exit(1);
    }

    // configure server address
    memset((char *) &serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(portno);
    if (inet_aton("127.0.0.1", &serv_addr.sin_addr) == 0) { // replace with server IP address
        perror("Error configuring server address");
        exit(1);
    }

    // retrieve random number from server
    int rand_num;
    socklen_t serv_len = sizeof(serv_addr);
    if (recvfrom(sockfd, &rand_num, sizeof(rand_num), 0, (struct sockaddr *) &serv_addr, &serv_len) < 0) {
        perror("Error receiving random number");
        exit(1);
    }

    // display random number
    printf("Received random number: %d\n", rand_num);

    close(sockfd);
    return 0;
}
