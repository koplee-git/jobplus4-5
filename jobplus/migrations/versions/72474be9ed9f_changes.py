"""changes

Revision ID: 72474be9ed9f
Revises: 487add61ea48
Create Date: 2018-04-10 23:20:52.526589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72474be9ed9f'
down_revision = '487add61ea48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resume', sa.Column('description', sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resume', 'description')
    # ### end Alembic commands ###
