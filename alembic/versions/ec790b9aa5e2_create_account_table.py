"""create account table

Revision ID: ec790b9aa5e2
Revises: 
Create Date: 2023-03-07 20:47:12.965902

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'ec790b9aa5e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'owners',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
    )

    op.create_table(
        'cars',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column(
            'owner_id', sa.Integer, sa.ForeignKey('owners.id'), index=True
        ),
        sa.Column('color', sa.String(50), nullable=False),
        sa.Column('model', sa.String(50), nullable=False),
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False, unique=True),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
        sa.Column('password', sa.String(100), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('cars')
    op.drop_table('owners')
