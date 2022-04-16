"""initial 2

Revision ID: b75dc0e63ca0
Revises: 2b8a19c577ff
Create Date: 2022-04-16 22:43:15.746142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b75dc0e63ca0'
down_revision = '2b8a19c577ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('pages', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'pages')
    # ### end Alembic commands ###
