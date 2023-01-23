from multiprocessing import Lock, Process, Queue, current_process
import time
import queue


def job_to_do(tasks_to_perform, complete_tasks):
    while True:
        try:
            # The try block to catch task from the queue.
            # The get_nowait() function is used to
            # raise queue.Empty exception if the queue is empty.
            task = tasks_to_perform.get_nowait()
        except queue.Empty:
            break
        else:
            # if no exception has been raised, the else block will execute
            # add the task completion
            print(task)
            complete_tasks.put(task + ' is done by ' + current_process().name)
            time.sleep(.5)
    return True


def main():
    total_task = 8
    total_number_of_processes = 3
    tasks_to_perform = Queue()
    complete_tasks = Queue()
    number_of_processes = []

    for i in range(total_task):
        tasks_to_perform.put("Task no " + str(i))

    # defining number of processes
    for w in range(total_number_of_processes):
        p = Process(target=job_to_do, args=(tasks_to_perform, complete_tasks))
        number_of_processes.append(p)
        p.start()

    # completing process
    for p in number_of_processes:
        p.join()

    # print the output
    while not complete_tasks.empty():
        print(": " + complete_tasks.get())

    return True


if __name__ == '__main__':
    main()
