from collections import OrderedDict
from functools import partial

from rich.progress import Progress, MofNCompleteColumn, TimeElapsedColumn, TransferSpeedColumn
from multiprocessing import Process, Queue

import aoc
from rangemap import RangeMap


def almanac(input):
    return OrderedDict({
        m.split('map:\n')[0].strip(): RangeMap.from_starts_and_lengths_str(m.split('map:\n')[1])
        for m in input.strip().split('\n\n')
        if not m.startswith('seeds:')
    })


def seed_to(seed, dest_map_name, almanac, debug=False):
    index = seed
    for key, correspondance in almanac.items():
        index = correspondance[index]
        if key == dest_map_name:
            return index
    return index


def seed_to_location(seed, almanac):
    return seed_to(seed, "humidity-to-location", almanac)


def seeds(input):
    return list(map(int, input.strip().split('\n')[0].split(':')[1].strip().split()))


def closest_location(seed_range, almanac, progress_queue, result_queue):
    result = []
    for i, seed in enumerate(range(seed_range[0], seed_range[0]+seed_range[1])):
        result.append(seed_to_location(seed, almanac=almanac))
        if i % 10000 == 0:
            progress_queue.put_nowait(10000)
    progress_queue.put_nowait(10000)
    result_queue.put_nowait(min(result))


if __name__ == "__main__":
    input = aoc.input(5)
    seed_ranges = list(zip(seeds(input)[::2], seeds(input)[1::2]))
    with Progress(
        *Progress.get_default_columns(),
        MofNCompleteColumn(),
        TransferSpeedColumn(),
        TimeElapsedColumn()
    ) as progress:
        tasks_progress = [progress.add_task(f"{seed_range}", total=seed_range[1]) for seed_range in seed_ranges]
        progress_queues = [Queue() for _ in range(len(seed_ranges))]
        result_queues = [Queue() for _ in range(len(seed_ranges))]

        tasks = [Process(target=closest_location, args=(seed_range, almanac(input), pq, rq))
                 for seed_range, pq, rq in zip(seed_ranges, progress_queues, result_queues)]

        for task in tasks:
            task.start()

        while not progress.finished:
            for i in range(len(progress_queues)):
                if not progress_queues[i].empty():
                    progress.update(tasks_progress[i], advance=progress_queues[i].get_nowait())

        for task in tasks:
            task.join()

        results = []
        for result_queue in result_queues:
            while not result_queue.empty():
                results.append(result_queue.get())

        print(min(results))
