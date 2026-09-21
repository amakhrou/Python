import os


def ft_tqdm(lst: range):
    total = len(lst)
    if total == 0:
        return

    try:
        columns = os.get_terminal_size().columns
    except AttributeError:
        columns = 80

    for i, item in enumerate(lst, 1):
        yield item

        percentage = int((i / total) * 100)

        fixed_len = 4 + 2 + 2 + len(str(i)) + len(str(total)) + 2 + 1
        bar_len = max(10, columns - fixed_len - 10)

        filled_len = int(bar_len * i // total)

        if filled_len > 0:
            bar = "-" * (filled_len - 1) + ">"
        else:
            bar = ""
        bar = bar.ljust(bar_len)

        output = f"{percentage:3d}%|[{bar}]| {i}/{total}"

        print(f"\r{output}", end="", flush=True)
    print()
