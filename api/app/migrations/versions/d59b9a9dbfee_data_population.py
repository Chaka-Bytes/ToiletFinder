"""data population

Revision ID: d59b9a9dbfee
Revises: 00876f524d89
Create Date: 2024-02-14 21:06:40.141690

"""
from typing import Sequence, Union
import json
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd59b9a9dbfee'
down_revision: Union[str, None] = '00876f524d89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with open('app/db/ibb.json', 'r') as f:
        data = json.load(f)
    
    for item in data:
        op.execute(
            sa.text(
                "INSERT INTO toilets (name, latitude, longitude) VALUES (:name, :latitude, :longitude)"
            ).bindparams(
                name=item.get('name'),
                latitude=item.get('latitude'),
                longitude=item.get('longitude')
            )
        )
    


def downgrade() -> None:
    pass
