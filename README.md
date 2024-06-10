# Wobidobi

Welcome to the repository of Wobidobi, your go-to free blogging platform where tech enthusiasts can publish articles, share insights, and engage with a community interested in technology. Wobidobi is built using Django and deployed on Digital Ocean, offering robust performance and reliability. This project is designed to be open-source and collaborative, inviting contributions from developers around the world.

**Live Site:** [Wobidobi](https://wobidobi.com/)

## Features

- **Free Article Publishing:** Users can publish articles and news about technology without any cost.
- **AI-Integrated Content Creation:** Utilize ChatGPT for drafting articles and generating content ideas.
- **Image Generation:** Enhance articles with AI-generated images to illustrate tech concepts.
- **Open Source:** Full source code available for anyone to use, modify, and distribute.
- **Community Driven:** A platform for users to share, collaborate, and improve the information shared.
- **Continuously Improving:** Regular updates to add new features and improve user experience.

## Technologies Used

- **Django:** A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Digital Ocean:** Hosting service providing scalable cloud hosting.
- **ChatGPT:** AI used for generating articles and assisting with content creation.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repo:
   ```sh
   git clone https://github.com/frollow/blog.git
   ```
2. Install Python packages:
   ```sh
   cd blog
   pip install -r requirements.txt
   ```
3. Setup your local environment:
   ```sh
   cp .env.example .env
   mv /blog/settings/environments/local.py.template /blog/settings/environments/local.py
   # Edit .env and local.py files with your settings
   ```
4. Migrate the database:
   ```sh
   python manage.py migrate
   ```
5. Run the development server:
   ```sh
   python manage.py runserver
   ```

Access the site at `http://127.0.0.1:8000/`.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

- Artem Frolov - tg: @ar_frolov
- Project Link: [https://github.com/frollow/blog](https://github.com/frollow/blog)