def wrap_text(text: str, limit: int) -> list[str]:
    words = text.split()
    lines, current_line = [], []

    for word in words:
        if sum(len(w) for w in current_line) + len(current_line) + len(word) <= limit:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))

    return lines

def justify_line(line: str, limit: int) -> str:
    if ' ' not in line or len(line) >= limit:
        return line

    words = line.split()
    spaces_needed = limit - len(line) + (len(words) - 1)
    slots = len(words) - 1
    space_distribution = [spaces_needed // slots] * slots

    for i in range(spaces_needed % slots):
        space_distribution[i] += 1

    justified = ''
    for word, space in zip(words, space_distribution + [0]):
        justified += word + ' ' * (space + 1)
    justified += words[-1]

    return justified.strip()

def justify_text(text: str, limit: int) -> list[str]:
    wrapped = wrap_text(text, limit)
    justified = [justify_line(line, limit) for line in wrapped[:-1]]
    justified.append(wrapped[-1])
    return justified
