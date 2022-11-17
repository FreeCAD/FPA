---
title: "Handbook Examples"
description:
    "Examples of Markdown"
layout: default
mermaid: true
---

# {{page.title}}

{{page.description}}


# Careful!

Don't use `[]` in YAML front matter.

`<img src="" width=80%>` will be rendered by typora but Jekyll only renders `<img src="" width="80%">`

Display math must have extra black lines above and below like this.

```markdown
some normal text

$$
E=mc^2
$$

Some more text
```

{% raw %}

do not use `{{` anywhere in your math. use `{ {` instead. Jekyll will parse that as liquid tags

do not use `x_1` in inline math, write that as `x _ 1`. Jekyll will parse that as italic.

{% endraw %}

# Highlights

*This is italic.* **This is Bold**. * If asterisk is surrounded by spaces, it is not parsed. *

_This is also italic._ __This is also Bold__. _ If underscore is surrounded by spaces, it is not parsed. _

~~This is strike through~~. 

There is no underline in markdown. You can use html tags <u>like this to underline.</u>

`This is a code block`. 

[This is an external link](https://bit.ly). "https://" is important. This is an internal [link](#this-is-a-h2). Internal links are all lowercase with space replaced by hyphens "-". 

You can mix them like [*this*](https://bit.ly), [`this`](https://bit.ly), **[this](https://bit.ly)**, but not like `[this](https://bit.ly)`.

# Blocks

> This is a quote block
>
> > This is a quote block in side another

```python
 import numpy as np
 print("""This is a python code fence""")
```

```fortran
 "This is a fortran code fence"
 implicit none
```

```
 This is a simple code fence. You can use it to display text. The fonts are mono spaced.
```

You can mix them as well, like 

> ```
>  This
> ```

# Other Elements

This is horizontal line

------


# Images

Markdown uses `![caption](link)` to reference pictures, caption is optional. You cannot control the size. 

![caption](https://raw.githubusercontent.com/yk-liu/yk-liu.github.io/master/_posts/2018-11-01-Introduction-to-Homology/assets/triangles.png)

So I prefer using HTML tags like this:

<img src="https://sliptonic.com/triangles.png" width="30%">

# Lists

- This is unordered list
  - sub item
    - subsub item
      - subsubsub item
        - subsubsubsub ...

------

- List can have multiple lines

  like this.

------

1. This ordered list
   1. sub item
2. This is as well
3. It can keep going

------

1. You can avoid numbers like this
   1. sub item
1. It keeps going
1. Blah Blah


# mermaid
[Mermaid](https://mermaid-js.github.io/mermaid/#/) let you describe diagrams using text. The actual image is generated automatically.

Code like:

```
sequenceDiagram
    Alice ->> Bob: Hello Bob, how are you?
    Bob-->>John: How about you John?
    Bob--x Alice: I am good thanks!
    Bob-x John: I am good thanks!
    Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

    Bob-->Alice: Checking with John...
    Alice->John: Yes... John, how are you?
```

Note: Actaual mermaid blocks start with three ticks and the word 'mermaid' and end with three ticks.

Yields a graph like:

```mermaid

sequenceDiagram
    Alice ->> Bob: Hello Bob, how are you?
    Bob-->>John: How about you John?
    Bob--x Alice: I am good thanks!
    Bob-x John: I am good thanks!
    Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

    Bob-->Alice: Checking with John...
    Alice->John: Yes... John, how are you?

```



```mermaid

sequenceDiagram
    Alice ->> Bob: Hello Bob, how are you?
    Bob-->>John: How about you John?
    Bob--x Alice: I am good thanks!
    Bob-x John: I am good thanks!
    Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

    Bob-->Alice: Checking with John...
    Alice->John: Yes... John, how are you?

```

```mermaid

graph LR
    A[Square Rect] -- Link text --> B((Circle))
    A --> C(Round Rect)
    B --> D{Rhombus}
    C --> D

```

```mermaid

graph TB
    sq[Square shape] --> ci((Circle shape))

    subgraph A subgraph
        od>Odd shape]-- Two line<br/>edge comment --> ro
        di{Diamond with <br/> line break} -.-> ro(Rounded<br>square<br>shape)
        di==>ro2(Rounded square shape)
    end

    %% Notice that no text in shape are added here instead that is appended further down
    e --> od3>Really long text with linebreak<br>in an Odd shape]

    %% Comments after double percent signs
    e((Inner / circle<br>and some odd <br>special characters)) --> f(,.?!+-*ز)

    cyr[Cyrillic]-->cyr2((Circle shape Начало));

     classDef green fill:#9f6,stroke:#333,stroke-width:2px;
     classDef orange fill:#f96,stroke:#333,stroke-width:4px;
     class sq,e green
     class di orange


```

```mermaid
sequenceDiagram
    loop Daily query
        Alice->>Bob: Hello Bob, how are you?
        alt is sick
            Bob->>Alice: Not so good :(
        else is well
            Bob->>Alice: Feeling fresh like a daisy
        end

        opt Extra response
            Bob->>Alice: Thanks for asking
        end
    end
```


# Tables

| This column is left aligned | This column is centered | This column is right aligned |
| :-------------------------- | :---------------------: | ---------------------------: |
| 1                           |            4            |                            7 |
| 2                           |            5            |                            8 |
| 3                           |            6            |                            9 |


# Foot Notes

This is a note[^1]. Footnotes can have captions like[^this]. You can reference to the same note multiple times like[^this]. Foot notes can have many other options like[^this-one]. Or just like [^that]. This is a [reference style link][linkid] to a page. And [this][linkid] is also a link. As is [this][] and [that].

# Titles

# This is  h1

## This is  h2

### This is  h3

#### This is  h4

##### This is h5

###### This is h6

# Foot Notes

The Foot notes are like this

[^1]: https://yk-liu.github.io
[^this]: https://yk-liu.github.io
[^this-one]: 

```
> Blockquotes can be in a footnote.
```

```
    as well as code blocks
```

[^that]: or, naturally, simple paragraphs.


