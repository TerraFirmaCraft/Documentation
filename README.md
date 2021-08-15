# [TerraFirmaCraft API Documentation](https://terrafirmacraft.github.io/Documentation/)

This is the host repository for the TerraFirmaCraft API documentation. It is intended for pack makers and addon developers who want to get information on how TFC (official and unofficial) APIs work.

Note: **this is not a wiki!** If you are a player of TFC-TNG, you will not find in-game documentation here. This is for developers of addons and packs using TFC-TNG. For gameplay documentation, consult the [wiki](https://tng.terrafirmacraft.com/Main_Page) instead.

### License

The Docsy-Jekyll Template is licensed under the Apache 2.0 License, and this is also released under the same license.

### Setup

Installation instructions are for WSL (Windows Subsystem for Linux), as Jekyll can be finicky on Windows. These notes are adapted from the [Jekyll installation instructions](https://jekyllrb.com/docs/), and various sources of installation help.

1. Install dependencies for ruby, and compiling the later gems.
  ```bash
  sudo apt install make gcc g++

  // This line was a fix noted from http://nokogiri.org/tutorials/installing_nokogiri.html
  sudo apt-get install zlib1g-dev liblzma-dev patch
  ```

1. Install Ruby. 
  ```bash
  sudo apt install ruby-full
  ```

2. Install the `jekyll` and `bundler` gems.
  ```bash
  sudo gem install jekyll bundler
  ```

3. Install required dependencies. Note: I have had issues with compiling the nokogiri gem, which was resolved by installing the 
  ```bash
  sudo bundle install
  ```

4. Run jekyll to serve the wiki locally
  ```bash
  bundle exec jekyll serve
  ```

5. Navigate to the server address to test. (`http://127.0.0.1:4000/Documentation/`)