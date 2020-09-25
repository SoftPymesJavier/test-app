"""Initial

Revision ID: 38f525df5990
Revises: 
Create Date: 2020-09-25 12:20:12.794357

"""
from alembic import op
import sqlalchemy as sa

from datetime import datetime


# revision identifiers, used by Alembic.
revision = '38f525df5990'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    table_example = op.create_table('example',
                                    sa.Column('exampleId', sa.Integer(), nullable=False),
                                    sa.Column('title', sa.String(length=50), nullable=False),
                                    sa.Column('description', sa.String(length=200), nullable=False),
                                    sa.Column('create_date', sa.DateTime(), nullable=True),
                                    sa.Column('update_date', sa.DateTime(), nullable=True),
                                    sa.PrimaryKeyConstraint('exampleId'),
                                    sa.UniqueConstraint('title'))

    op.bulk_insert(table_example, init_data)


def downgrade():
    op.drop_table('example')


################
# INITIAL DATA #
################
init_data = [
    {
        'exampleId': 1,
        'title': 'First Title',
        'description': 'First Description',
        'create_date': datetime.now(),
        'update_date': datetime.now()
    }
]
