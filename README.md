# ShitIsaid.com

----

##### Shitisaid.com is a free-to-use transcripts amalgamator.

##### It accepts a wide range of artifacts, converts them to transcripts, and allows

##### the user to store, browse, and access them easily and conveniently online.

##### The website accepts a variety of text, audio, and video formats, as well as URLs for maximum convenience!

----

### Architecture

##### This application runs 3 parallel docker containers. Frontend, Backend, and Database.

##### They communicate via pre-established exposed ports. Separation improves control, scaling, and performance.

### Installation

You need [Docker](https://docs.docker.com/get-docker/) with the Compose plugin.
```
git clone https://github.com/shitisaid-com/shitisaid.com.git
cd shitisaid.com
cp .env.example .env
```

### Configuration

All settings live in `.env`, you'll need to set these before you can run anything:

| Variable            | Purpose                                |
| ------------------- | -------------------------------------- |
| `POSTGRES_USER`     | Database user created on first start   |
| `POSTGRES_PASSWORD` | Password for that user                 |
| `POSTGRES_DB`       | Name of the database created on first start |

These values are only used when the database is created for the first time.

**Version:** PostgreSQL 18 (`postgres:18`), pinned to the major version. Don't change it to `latest`: a new major version can't read existing data without a manual upgrade.

**Ports:** the database is published on `localhost:5432` which is the default port. Other containers reach it at `db:5432`, not `localhost`.

**Schema:** Create a 'db_init' folder and put the `.sql` files inside, then uncomment the `db_init` line in `compose.yaml`. This will create the databases from the schema on the first run.

### Basic Commands:

```
docker compose up -d          # start in the background
docker compose ps             # check status
docker compose logs -f db     # follow database logs
docker compose down           # stop (data is kept)
```

Connect to the database:

```
docker compose exec db psql -U <POSTGRES_USER> <POSTGRES_DB>
```

Data is stored in the `pgdata` Docker volume, so it survives restarts and `docker compose down`.

To **wipe the database** and start fresh run `docker compose down -v`. This will wipe all data in the database.

----

## For Developers

### How to contribute?

1. Assign yourself a ticket on our [kanban]([Sign in — Kommit](https://kommit.mccrimmon.me/projects/stuffisaid/board)). Make sure it's assigned to you before you begin working on it!
2. Navigate to the directory with your cloned repository
3. checkout to main and run `git pull` to make sure your main branch is up to date (**very important**)
4. Take the number seen on the ticket and precede it with `T-` to (in this case) get `T-100` . Then create a new branch with this name using `git branch T-100`.
   
   <img title="" src="assets/1.png" alt="1.png" width="360">
   
   
5. You can now checkout to your newly created branch with `git checkout T-100`, and begin work on the ticket!
6. Once requirements have been met, you can submit the ticket for a [pull request](https://docs.github.com/en/pull-requests/reference/pull-requests) on our [github page]([Pull requests · shitisaid-com/shitisaid.com · GitHub](https://github.com/shitisaid-com/shitisaid.com/pulls)). Simply click "New pull request" and follow the wizard.
   
   <img title="" src="assets/2.png" alt="2.png" width="218">
   
   
7. **Always make sure main is on the left-hand side**. You're pushing TO main, not FROM it.
   
   ![3.png](assets/3.png)
   
   
8. If you see any merge conflicts, feel free to contact the rest of the team members. Those can be real bitches to solve.
   
   
   
   
