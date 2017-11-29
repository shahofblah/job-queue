# job-queue
Job queue, worker and client processes to run Docker images

Each process can run on a separate host.
Each worker and client process must be associated with a single queue process.
The values in Common/Endpoints.py must reflect the address and port number of the queue process for clients and workers to be able to access it.