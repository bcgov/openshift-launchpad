Generic single-database configuration.

When you make changes to the model or add new model, run ```flask db migrate -m "messages."```

To update the database run: ```flask db upgrade```

To rollback changes run ```flask db downgrade```

Running migrations through Docker:

```docker-compose start server-migrate``` or ```make db-upgrade```