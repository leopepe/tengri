# Tengri AWS TrickBox and Supervisor

Tengri is a tool to perform simples tasks and automate routines onto an AWS VPC.

Example:
    - Stop or Terminate all instances based on their KeyPair name.
    - Schedule a report about live instances by project (identified by KeyPair name)

## Overview

Features:

- List all instances which key pair name is not on the exclude list
- Stop all instances which key pair name is not on the exclude list