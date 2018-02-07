def reverse(input: str = '') -> str:
    if not input:
        return ''
    return reverse(input[1:]) + input[0]
