# How to upload slides
- Clone this repo directory (you should have push access!)
- Run `python add_lecture.py` and follow the prompt
- Git add, commit, push


# How to use jekyll to display site locally

```bash
brew install ruby
bundle install
bundle exec jekyll serve --baseurl ''
```

Then, open [`localhost:4000`](http://localhost:4000) in your browser.


The syllabus is maintained in `_data/lectures.yml` and the announcements are contained in `_data/announcements.yml`.
