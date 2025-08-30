# URL Checker & Backlink Tool (URL有效性检测 & 外链批量添加工具)

A multi-threaded tool to check the availability of URLs. Its primary feature is to **instantly add over 2900+ backlinks** to your domain with a single command.

多线程URL有效性检测工具。其核心功能是 **通过一条命令，一键为您的网站批量增加超过2900个外链**。

## Key Features (核心功能)

  * **One-Command Backlinks**: Instantly generate and verify over 2900 backlinks for your website.
      * **一键添加外链**：通过一条命令，即刻为您的网站生成并验证超过2900个反向链接。
  * **URL Availability Check**: Check the status of URLs from a local file (`.txt`) or a remote webpage.
      * **URL有效性检测**：支持检测来自本地文件（`.txt`）或在线网页中的URL列表。
  * **Multi-threaded**: Utilizes multi-threading for high-speed checking.
      * **多线程处理**：利用多线程技术，实现高速批量检测。
  * **Automatic Sorting**: Automatically categorizes results into `valid`, `broken`, and `special error` files.
      * **结果自动分类**：检测结果会自动分类为有效、失效和特殊错误三种文件。

## 🔧 Requirements (环境需求)

> Python 3

## Usage (用法)

### Primary Feature: Adding 2900+ Backlinks (核心功能：添加2900+外链)

This is the main purpose of this tool. The included `backlinks.txt` file contains over 2900 URLs where `hoothin` is used as a placeholder. The following command replaces this placeholder with your domain, effectively creating and checking a massive list of backlinks for your site.

这是本工具的核心。项目自带的 `backlinks.txt` 文件包含了超过2900条URL，并使用 `hoothin` 作为占位符。以下命令会将占位符替换为您自己的域名，从而为您的网站批量生成并验证海量外链。

```bash
python url_checker.py -b your-domain.com
```

### General URL Checking (常规URL检测)

You can also use this tool for general URL status checking.
你也可以使用本工具进行常规的URL有效性检测。

  * **Check URLs from a local file (检测本地文件)**:

    > The `.txt` file should contain one URL per line.
    > `.txt` 文件内应每行包含一个URL。

    ```bash
    python url_checker.py url.txt
    ```

  * **Check URLs from a remote file/page (检测在线URL)**:

    > This will find and check all URLs on the specified webpage.
    > 此命令会收集并验证指定网页中包含的所有URL。

    ```bash
    python url_checker.py https://example.com/urls.txt
    ```

## Output Results (结果说明)

Three `.txt` files will be generated in the script's directory.
脚本运行后，会在当前目录下生成三个`.txt`文件。

| File (文件)         | Content (内容)                                         |
| ----------------- | -------------------------------------------------------- |
| `result.txt`      | Valid URLs (有效URL)                                     |
| `urlBroken.txt`   | Broken or inaccessible URLs (失效或无法访问的URL)          |
| `urlJsError.txt`  | URLs blocked by specific firewalls (e.g., Jiangsu) (撞上江苏内墙等特殊错误的URL) |